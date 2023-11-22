from collections import defaultdict
from typing import List

class UnionFind():
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = self.root[rootY]
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = self.root[rootX]
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_idx = defaultdict(int)
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_to_idx:
                    email_to_idx[email] = i
                else:
                    uf.union(i, email_to_idx[email])

        for i in range(len(accounts)):
            uf.find(i)

        output = []
        
        merge_acc = defaultdict(set)

        for i, root_idx in enumerate(uf.root):
            name = accounts[root_idx][0]
            for email in accounts[root_idx][1:]:
                merge_acc[(root_idx, name)].add(email)
            for email in accounts[i][1:]:
                merge_acc[(root_idx, name)].add(email)

        for (_, name), set_email in merge_acc.items():
            emails = list(set_email)
            emails.sort()
            output.append([name] + emails)

        return output
    
# SOLUTION
from collections import defaultdict

def accounts_merge(accounts):
    # initialize a constructor that will create the parents array with unique IDs
    uf = UnionFind(len(accounts))
    
    # create a map for mapping emails to their parent IDs
    email_mapping = {}
    for i, account in enumerate(accounts):
        emails = account[1:]
        for email in emails:

            # if the email already exists in the map, take union
            if email in email_mapping:

                # before we take the union, make sure both the accounts have the same name 
                if account[0] != accounts[email_mapping[email]][0]: 
                    return
                uf.union(email_mapping[email], i)

            # add email with its ID to the map
            email_mapping[email] = i
        
    # create a map to store the merged accounts
    merged_accounts = defaultdict(list)
    for email, ids in email_mapping.items():
        merged_accounts[uf.find(ids)].append(email)

    # sort the merged accounts
    final_merged =[]
    for parent, emails in merged_accounts.items():
        final_merged.append([accounts[parent][0]]+sorted(emails))
    return final_merged

# driver code
def main():
    all_accounts = [[["Emma", "emma@mail.com", "emma_work@mail.com"], ["Bob", "bob_home@mail.com", "bob123@mail.com"], ["Emma", "emma_art@mail.com", "emma_work@mail.com"], ["Bob", "bob321@mail.com"]],
                    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
                    [["Sarah", "sarah@mail.com", "sh@mail.com"],["Sarah", "sarah1@mail.com", "sarahh@mail.com"], ["Sarah", "sh3@mail.com"]],
                    [["Alice", "alice@mail.com"], ["Alice", "alice_alice@mail.com", "alice@mail.com"], ["Alice", "alice@mail.com", "alice123@mail.com", "aalicee@mail.com"]],
                    [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]]
    
    for i in range(len(all_accounts)):
        print(i+1, ".\tAccounts: \n\t[", sep="")
        for a in all_accounts[i]:
            print("\t",a)
        print("\t]")
        
        merged = accounts_merge(all_accounts[i])
        
        if(merged == None):
            print("Error!\nAccounts sharing some email(s) should have the same names.")
            return

        print("\n\tMerged accounts: \n\t[")
        for m in merged:
            print("\t",m)
        print("\t]")
        print("-" * 100)

if __name__ == '__main__':
        main()