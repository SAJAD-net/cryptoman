# CRYPTOMAN

## Ceaser Cipher
Ceaser Ciper is one of the simplest and most widely known encryption techniques.</br>
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.</br>
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.</br>
The method is named after Julius Caesar, who used it in his private correspondence.</br>
[To learn more (Wikipedia)](https://en.wikipedia.org/wiki/Caesar_cipher)


## Vigenère Cipher
The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.</br>

For example, if the plaintext is <b>attacking tonight</b> and the key is <b>OCULORHINOLARINGOLOGY</b>, then

  the first letter a of the plaintext is shifted by 14 positions in the alphabet (because the first letter <b>O</b> of the key is the 14th letter of the alphabet, counting from zero), yielding <b>o</b>.</br>
  the second letter t is shifted by 2 (because the second letter <b>C</b> of the key means 2) yielding <b>v.</b></br>
  the third letter t is shifted by 20 (<b>U</b>) yielding <b>n</b>, with wrap-around.</br>

and so on; yielding the message ovnlqbpvt hznzouz.</br>
If the recipient of the message knows the key, they can recover the plaintext by reversing this process.</br>
[To learn more (Wikipedia)](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
