import igo

PLACE = 'Barcelona, Catalonia'
GRAPH_FILENAME = 'barcelona.graph'
SIZE = 500
HIGHWAYS_URL = 'https://opendata-ajuntament.barcelona.cat/data/dataset/1090983a-1c40-4609-8620-14ad49aae3ab/resource/1d6c814c-70ef-4147-aa16-a49ddb952f72/download/transit_relacio_trams.csv'
CONGESTIONS_URL = 'https://opendata-ajuntament.barcelona.cat/data/dataset/8319c2b1-4c21-4962-9acd-6db4c5ff1148/resource/2d456eb5-4ea6-4f68-9794-2f3f1a58a933/download'



highways = igo.download_highways(HIGHWAYS_URL)
#igo.plot_highways(highways, 'highways.png', SIZE)

#print(len(highways))

#download congestions and plot them into a PNG image
congestions = igo.download_congestions(CONGESTIONS_URL)
#print(len(congestions))
#igo.plot_congestions(highways, congestions, 'congestions.png', SIZE)


#G = igo.load_graph("barcelona.graph")

#for edge in G.edges:
    #try:
        #print(type(G.edges[edge[0], edge[1]]['length']))
    #except:
        #print(G.edges[edge[0], edge[1]])
#igo.nx.set_edge_attributes(G, -1, "congestion")

#igraph = igo.build_igraph(G, highways, congestions)
#igo.spread_congestions(G, highways, congestions)

igraph = igo.load_graph("igraph.graph")

# get 'intelligent path' between two addresses and plot it into a PNG image
#ipath = igo.get_shortest_path_with_ispeeds(igraph, "Carrer del Sagrat Cor 25", "upc campus nord")
ipath = [30960621, 30960622, 402894803, 30960624, 412449344, 359100760, 30960627, 690812143, 30960642, 2463014352, 415956313, 415956317, 415956315, 415956314, 415956316, 415956323, 415956312, 2480495525, 2881600611, 3713384673, 690803404, 1695056489, 30254079, 30295259, 30254080, 30254081, 30254082, 30254083, 30254084, 30254085, 667410900, 30555974, 30243391, 1860476035]
igo.plot_path(igraph, ipath, size=SIZE)



#for node1, info1 in igraph.nodes.items():
    #print(igraph.nodes[node1])
    # for each adjacent node and its information...
    #for node2, edge in G.adj[node1].items():
        #print('    ', node2)
        #print('        ', edge)

#igo.plot_graph(graph)
