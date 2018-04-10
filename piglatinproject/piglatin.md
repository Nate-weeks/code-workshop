Nate and N's Pig Latin Translator
==============

Assignment
===========

Working with the others in your group, design and implement an industrial strength piglatin text conversion utility, which you will present in class. Include

A specification of what your utility does.  Documentation on how to install and use it.  Test cases and examples.
I also want you to think of this effort as an exercise in project management, so be thinking about how you're making decisions, how you're sharing the work, and what software tools you're choosing to use.

Research
=============

Googled the wiki entry on Pig Latin and chose from a few of the optional rules on how to handle vowels and other edge-cases.

* [https://en.wikipedia.org/wiki/Pig_Latin](https://en.wikipedia.org/wiki/Pig_Latin)

Rules and Examples
=============

Piglatin rules:

1:  Words that begin with single consonants, consonants are removed at the beginning of the word and put at the end with "ay" attached

examples:
* dog ---> ogday
* cat ---> atcay
* time ---> imetay

2:  Words that begin with double consonants or consonant clusters, clusters are removed - added to the end of the word with "ay" attached

examples:
* chat ---> atchay
* stupid ---> upidstay
* smart ---> artsmay

3:  Words that begin with vowels, words stay - [ ] he same with "way" added to the end

examples:  
* end ----> endway
* another ---> anotherway

4:  Words that start in a capital letter still have the capital at the beginning

examples:
* Capital ---> Apitalcay
* Apple ---> AppleWay

5:  qu counts as one letter and stays together

examples:
* queen ---> eenquay
* quality ---> alityquay

6:  Numbers are ignored, but numbers like 5th, 6th, 7th have way added to the end as if they are vowels

examples:
* 7th ---> 7thway
* 123 ---> 123

7:  Y is counted as a consonant.

examples:
* Yes ---> esyay
* yard ---> ardyay

8: Vowels or consanants with accents are treated as their normal counterparts

examples:
* änother škit ---> änotherway itškay
