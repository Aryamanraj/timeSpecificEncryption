# Time Specific Encryption
This system takes the idea of the Research Paper by Kenneth G. Paterson & Elizabeth A. Quaglia published in Springer. 

[Time-Specific Encryption](https://link.springer.com/chapter/10.1007/978-3-642-15317-4_1#:~:text=In%20(Plain)%20TSE%2C%20a,a%20time%20in%20that%20interval.)

### Plain Time-Specific Encryption

In Time-Sensitive Encryption (TSE), a key, known as a Time Instant Key (TIK), is broadcasted by a Time Server at the start of each time unit. When sending a message, the sender can choose a specific time period, and the recipient can only decrypt the message if they have a TIK that corresponds to a time within that period. Our approach extends TSE to the public-key and identity-based settings, where the receivers have private keys, public keys or identities and the decryption process requires the use of private key and a valid TIK.

### The system is divided into two sections: 
* Time-Server
* Encryption API

### Time Server
It is a separate server hosted by 
