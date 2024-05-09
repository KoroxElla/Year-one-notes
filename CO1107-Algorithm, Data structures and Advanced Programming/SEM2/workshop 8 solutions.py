class TreeNode:
    def __init__(self,item=None):
        self.item=item
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self, root):
        self.root=root



# The size of the Tree

    def __len__(self):
        return self.len_aux(self.root)
    def len_aux(self,current):
        if current is None:
            return 0
        else:
            return 1+self.len_aux(current.left)+self.len_aux(current.right)

#The height of Tree

    def height(self):
        return self.height_aux(self.root)
    def height_aux(self,current):
        if current is None:
            return -1
        else:
            return 1+max(self.height_aux(current.left), self.height_aux(current.right))
    

#The sum of leaves

    
    def sum_leaves(self):
        return self.sum_leaves_aux(self.root)
    def sum_leaves_aux(self,current):
        if current is None:
            return 0
        elif current.left is None and current.right is None:
            return current.item
        else:
            return self.sum_leaves_aux(current.left)+ self.sum_leaves_aux(current.right)

# Count the number of leaves

    def count_leaves(self):
        return self.count_leaves_aux(self.root)
    def count_leaves_aux(self,current):
        if current is None:
            return 0
        elif current.left is None and current.right is None:
            return 1
        else:
            return self.count_leaves_aux(current.left)+ self.count_leaves_aux(current.right)


# print all the elements of the Tree

    def print_preorder(self):
        self.print_preorder_aux(self.root)
    def print_preorder_aux(self,current):
        if current is not None:
            print(current.item)
            self.print_preorder_aux(current.left)
            self.print_preorder_aux(current.right)

# returns those nodes less than a given value k.

    def nodes_less_than(self,k):
        aList=[]
        self.tree_check_aux(self.root,k,aList)
        return aList
    def tree_check_aux(self,current,k, aList):
        if current is not None:
            if current.item <k :
                aList.append(current.item)
            self.tree_check_aux(current.left, k,aList)
            self.tree_check_aux(current.right, k, aList)



# returns true if the tree contains the integer i, and false otherwise.
 
    def tree_contains(self,target):
        return self.tree_contains_aux(self.root,  target)
        
    def tree_contains_aux(self,current, target):
        if current is None:
            return False
        elif current.left is None and current.right is None:
            return (target==current.item)
        else:
            if target==current.item: return True
            else:
                return (self.tree_contains_aux(current.right, target) or self.tree_contains_aux(current.left, target))


     

    def is_balanced(self):
        return self.is_balanced_aux(self.root)
    def is_balanced_aux(self,current):
            if current is None:
                return True
            else:
                dif = self.height_aux(current.left) - self.height_aux(current.right)
                
                if abs(dif) > 1:
                    return False
                else:
                    return self.is_balanced_aux(current.left) and self.is_balanced_aux(current.right)


                   


ex1=TreeNode(1)
bt=BinaryTree(ex1)
ex1.left=TreeNode(2)
ex1.right=TreeNode(3)
ex1.left.left=TreeNode(4)
ex1.left.right=TreeNode(5)
#ex1.right=TreeNode(5)
#ex1.right.left=TreeNode(6)
#ex1.right.right=TreeNode(7)
#ex1.right.right.right=TreeNode(8)
#ex1.right.right.left=TreeNode(9)
#ex1.right.right.right.right=TreeNode(10)
#ex1.right.right.right.left=TreeNode(11)

print("The size of the binary tree is : ", bt.__len__())
print("The height of the Tree is : ",bt.height())
print("The number of the leaves is : ",bt.count_leaves())
print("The sum of the leaves is : ",bt.sum_leaves())

print("Does the Tree containt 5: ",bt.tree_contains(5))

print("The nodes less than 3 are : ", bt.nodes_less_than(3))
print(bt.is_balanced())

bt.print_preorder()
