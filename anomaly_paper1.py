from __future__ import print_function, division
from igraph import *
import numpy as np

__author__ = 'panzer'

def say(*lst):
  print(*lst, end="")
  sys.stdout.flush()

def list_files(folder):
  """
  List all files in a folder
  :param folder: Name of the folder
  :return: list of complete file names in folder
  """
  return ["%s/%s"%(folder, f) for f in os.listdir(folder) if f.endswith(".txt")]

def make_graph(file_name):
  """
  Make graph from a file
  :param file_name:
  :return:
  """
  with open(file_name, 'r') as f:
    lines = f.readlines()
    node_count, edge_count = map(int, lines[0].strip().split())
    edges = [map(int, line.strip().split()) for line in lines[1:]]
    graph = Graph()
    graph.add_vertices(node_count)
    graph.add_edges(edges)
  return graph

def _main(folder):
  graphs = []
  for f in list_files(folder):
    graphs.append(make_graph(f))



if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("USE THE COMMAND : python anomaly.py <data folder>")
    exit()
  folder_name = args[1]
  _main(folder_name)