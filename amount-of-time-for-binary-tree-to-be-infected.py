# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_graph(self, root):
        queue = deque()
        queue.append([root, None])
        graph = defaultdict(list)
        infected_node = None
        while queue:
            node, parent = queue.popleft()
            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node:
                if node.left:
                    queue.append([node.left, node])
                if node.right:
                    queue.append([node.right, node])
        return graph

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = self.build_graph(root)
        queue = deque()
        queue.append(start)
        infect = set()
        infect.add(start)
        minute = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                infect.add(node)
                for nei in graph[node]:
                    if nei not in infect:
                        queue.append(nei)
            
            minute += 1
        
        return minute - 1
            
# one pass with DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root, start):
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, root, start):
        depth = 0
        if root is None:
            return depth

        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)

        if root.val == start:
            self.max_distance = max(left_depth, right_depth)
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1

        return depth
                
        
