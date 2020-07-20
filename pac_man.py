#pac man problem
import numpy as np
inp=[['#','#','#','#','#','#','#','#'],['#','-','-','-','-','-','-','#'],['#','-','#','#','#','-','-','#'],['#','-','#','*','#','-','-','#'],['#','-','-','-','#','-','-','#'],['#','-','#','#','#','-','-','#'],['#','p','-','-','-','-','-','#'],['#','#','#','#','#','#','#','#']]
inp=np.array(inp)
start=[6,1]
goal=[3,3]

def possible_operation_and_perform(Matrix,start):
  operation=[]
  temp=[-1,-1]
  if(Matrix[start[0]][start[1]-1]!='#'):
    temp=[start[0],start[1]-1]
    operation.append(temp)
  if(Matrix[start[0]][start[1]+1]!='#'):
    temp=[start[0],start[1]+1]
    operation.append(temp)
  if(Matrix[start[0]-1][start[1]]!='#'):
    temp=[start[0]-1,start[1]]
    operation.append(temp)
  if(Matrix[start[0]+1][start[1]]!='#'):
    temp=[start[0]+1,start[1]]
    operation.append(temp) 
  return operation
def search_tree(Matrix,start,goal):
  path=[]
  graph=[]
  stack=[]
  stack.append(start)
  path=[]
  while(True):
    start=stack.pop(0)
    
    if(start not in path):
      path.append(start)
    if(start==goal):
      break
    operation=possible_operation_and_perform(Matrix,start)
    for i in operation:
      if(i in path):
        continue
      temp=[]
      temp.append(start)
      temp.append(i)
      if(temp not in graph):
        graph.append(temp)
      stack.append(i)
  return graph

def bfs(graph,start,goal):
  stack=[]
  path=[]
  stack.append(start)
  while(True):
    start=stack.pop(0)
    path.append(start)

    if(start==goal):
      break
    for i in graph:
      if(i[0]==start):
        if(i[1] not in stack and i[1] not in path):
          stack.append(i[1])
  return path
def dfs(graph,start,goal):
  stack=[]
  path=[]
  stack.append(start)
  while(True):
    start=stack.pop(0)
    path.append(start)

    if(start==goal):
      break
    for i in graph:
      if(i[0]==start):
        if(i[1] not in stack and i[1] not in path):
          stack.insert(0,i[1])
  return path

def search_path(path,start,goal):
  s=[]
  s.append(goal)
  ans=[]
  while(True):
    s1=s.pop(0)
    ans.insert(0,s1)
    if(s1==start):
      break
    for i in path:
      if(i[1]==s1 and i[0] not in s):
        s.append(i[0])
  print("backtracking search for optimal path",ans)

graph=search_tree(inp,start,goal)
print("search tree or tree on which we can apply bfs and dfs\n")
for i in graph:
  print(i)
path_bfs=bfs(graph,start,goal)
print("bfs search path",path_bfs)
path_dfs=dfs(graph,start,goal)
print("dfs search path",path_dfs)

#using backtracking
def search_path(path,start,goal):
  s=[]
  s.append(goal)
  ans=[]
  while(True):
    s1=s.pop(0)
    ans.insert(0,s1)
    if(s1==start):
      break
    for i in path:
      if(i[1]==s1 and i[0] not in s):
        s.append(i[0])
  print("backtracking search for optimal path",ans)
search_path(graph,start,goal)
