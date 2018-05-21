import ast
import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def fetch_list_of_fnames(path):
    list_of_fnames = []

    for dirname, dirs, files in os.walk(path, topdown=True):
        for fname in files:
            if fname.endswith('.py'):
                list_of_fnames.append(os.path.join(dirname, fname))
    logger.info(f'total {len(list_of_fnames)} files')
    return list_of_fnames


def fetch_list_of_trees(path):
    list_of_fnames = fetch_list_of_fnames(path)

    list_of_trees = []

    for fname in list_of_fnames:
        with open(fname, 'r', encoding='utf-8') as current_file:
            current_fcontent = current_file.read()
        try:
            tree = ast.parse(current_fcontent)
        except SyntaxError as error:
            print(error)
            continue
        list_of_trees.append(tree)
    logger.info('trees generated')
    return list_of_trees


class FuncGetter(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.list_of_nodes = []

    def visit_FunctionDef(self, node):
        self.list_of_nodes.append(node)
        self.generic_visit(node)

    def get_function_names(self):
        return [node.name.lower() for node in self.list_of_nodes]


class VarGetter(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.list_of_nodes = []

    def visit_Name(self, node):
        self.list_of_nodes.append(node)
        self.generic_visit(node)

    def get_variable_names(self):
        return [node.id.lower() for node in self.list_of_nodes]


def fetch_list_of_node_names(path, type_of_node='function'):
    list_of_trees = fetch_list_of_trees(path)

    function_getter = FuncGetter()

    for tree in list_of_trees:
        function_getter.visit(tree)

    output = []

    if type_of_node == 'function':
        for function_name in function_getter.get_function_names():
            if not (function_name.startswith('__') and
                    function_name.endswith('__')):
                output.append(function_name)
        logger.info(f'total {len(output)} {type_of_node}s')
        return output

    if type_of_node == 'variable':
        var_getter = VarGetter()
        for function in function_getter.list_of_nodes:
            var_getter.visit(function)
        output = var_getter.get_variable_names()
        logger.info(f'total {len(output)} {type_of_node}s')
        return output
