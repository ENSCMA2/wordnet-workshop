import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

motorcar = wn.synsets('motorcar')
print('synsets that motorcar belongs to: ' + motorcar)
cars = wn.synset('car.n.01')
print('synset of car sense 1: ' + cars)
print('car sense 1 lemma names: ' + cars.lemma_names())
print('car sense 1 definition: ' + cars.definition())
print('car sense 1 example sentences: ' + cars.examples())
car_lemmas = cars.lemmas()
print('car sense 1 lemmas: ' + car_lemmas)
automobile = wn.lemma('car.n.01.automobile')
print('synset of automobile (car sense 1): ' + automobile.synset())
print('name of the automobile lemma: ' + automobile.name())

all_noun_synsets = wn.all_synsets('n')
print('number of noun synsets: ' + str(len(all_noun_synsets)))

car_synsets = wn.synsets('car')
print('synsets that car belongs to: ' + car_synsets)
for synset in car_synsets:
	print(synset + ' ' + synset.lemma_names())

print('synsets in which car is a lemma: ' +  wn.lemmas('car'))

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print('types of motorcars: ' + repr(types_of_motorcar))
print('types of motorcars along with their synonyms: ' + repr(sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()])))

print('motorcar hypernyms: ' + motorcar.hypernyms())
print('motorcar root hypernyms: ' + motorcar.root_hypernyms())
paths = motorcar.hypernym_paths()
print('first possible path from motorcar to a hypernym: ' + paths[0])
print('second possible path from motorcar to a hypernym:' + paths[1])

tree = wn.synset('tree.n.01')
tree_parts = tree.part_meronyms()
print('parts of a tree: ' + tree_parts)
tree_ingredients = tree.substance_meronyms()
print('materials in a tree: ' + tree_ingredients)
tree_groups = tree.member_holonyms()
print('tree holonyms: ' + tree_groups)

walk = wn.synset('walk.v.01')
walk_entail = walk.entailments()
print('what walking entails: ' + walk_entail)

supply = wn.lemma('supply.n.02.supply')
not_supply = supply.antonyms()
print('antonyms of supply: ' + not_supply)

right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')

right_minke = right.lowest_common_hypernyms(minke)
print('right & minke are both: ' + right_minke)
right_orca = right.lowest_common_hypernyms(orca)
print('right & orca are both: ' + right_orca)
right_tortoise = right.lowest_common_hypernyms(tortoise)
print('right & tortoise are both: ' + right_tortoise)
right_novel = right.lowest_common_hypernyms(novel)
print('right & novel are both: ' + right_novel)

print('minimum semantic distance from right to minke: ' + right_minke.min_depth())
print('minimum semantic distance from right to orca: ' + right_orca.min_depth())
print('minimum semantic distance from right to tortoise: ' + right_tortoise.min_depth())
print('minimum semantic distance from right to novel: ' + right_novel.min_depth())

right_minke_similarity = right.path_similarity(minke)
print('similarity between right and minke: ' + right_minke_similarity)
right_orca_similarity = right.path_similarity(orca)
print('similarity between right and orca: ' + right_orca_similarity)
right_tortoise_similarity = right.path_similarity(tortoise)
print('similarity between right and tortoise: ' + right_tortoise_similarity)
right_novel_similarity = right.path_similarity(novel)
print('similarity between right and novel: ' + right_novel_similarity)
