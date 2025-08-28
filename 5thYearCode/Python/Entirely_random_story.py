from random import * # The tall boy is walking quickly to the shop

articles=(["a","my","that","the","your"])
adjective=choice(["annoying","baby","buff","chav","cheeky","clever","curious","elderly","English","fat","French","hairy","humungus","Irish","jacked","Minecraft","posh","sexy","short","skinny","smart ass","Spanish","stupid","sweaty","tall","young"])
noun=choice(["alien","ass","boy","cat","chicken","Cork Man","cow","dog","elephant","giraffe","girl","horse","Jedi","kangaroo","man","mouse","pig","Ryan","sheep","Sith","teacher","turkey","woman","X-Factor contestant","zebra"])
tense=choice(["is","was","will be","used to be"])
verb=choice(["crapping","dancing","digging","driving","flying","jogging","naruto running","pooing","running","singing","swimming","walking"])
adverb=choice(["angrily","cheerfully","gracefully","happily","like a ninja","magestically","quickly","slowly","swiftly"])
proposition=choice(["away from","into","near","passed","towards"])
#ARTICLE2 IS HERE
place=choice(["club","church","docks","jail","library","microwave","museum","police station","prison","school","shop","shopping centre","sport centre","stadium"])

article1 = choice(articles)
article2 = choice(articles)

print(article1, adjective, noun, tense, verb, adverb, proposition, article2, place)

if tense==("used to be"):
    print("but not anymore")