class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        res = " " * level + str(self.data) + '\n'
        for child in self.children:
            res += child.__str__(level + 1)
        return res 

    def addChild(self, TreeNode):
        self.children.append(TreeNode)



if __name__ == "__main__":

    tree = TreeNode("drinks", [])
    cold = TreeNode("cold", [])
    hot = TreeNode('hot', [])
    tree.addChild(cold)
    tree.addChild(hot)
    tea = TreeNode('tea', [])
    coffee = TreeNode('coffee', [])
    cola = TreeNode('cola', [])
    fanta = TreeNode('fanta', [])
    hot.addChild(tea)
    hot.addChild(coffee)
    cold.addChild(cola)
    cold.addChild(fanta)

    print(tree)