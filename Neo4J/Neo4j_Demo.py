from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j","Pa55word"))
session = driver.session()

rows = session.run("""
MATCH (n:Character) RETURN n LIMIT 2
""")
for row in rows:
    print row
    print row["n"]
    print row["n"].id
    print row["n"].labels
    print row["n"]["name"]
    print "----------------"
# 标准输出
# <Record n=<Node id=27 labels=set([u'Character']) properties={u'name': u'Addam-Marbrand'}>>
# <Node id=27 labels=set([u'Character']) properties={u'name': u'Addam-Marbrand'}>
# 27
# frozenset([u'Character'])
# Addam-Marbrand
# ----------------
# <Record n=<Node id=28 labels=set([u'Character']) properties={u'name': u'Aegon-Frey-(son-of-Stevron)'}>>
# <Node id=28 labels=set([u'Character']) properties={u'name': u'Aegon-Frey-(son-of-Stevron)'}>
# 28
# frozenset([u'Character'])
# Aegon-Frey-(son-of-Stevron)
# ----------------


# episodes = {}
# for row in rows:
#     if episodes.get(row["id"]["id"]) is None:
#         if row["appearance"] is None:
#             episodes[row["id"]["id"]] = [0]
#         else:
#             episodes[row["id"]["id"]] = [1]
#     else:
#         if row["appearance"] is None:
#             episodes[row["id"]["id"]].append(0)
#         else:
#             episodes[row["id"]["id"]].append(1)
#
# print len(episodes)
# print len(episodes[0])
# print episodes[1]
