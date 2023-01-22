# Time Specific Encryption
This system takes the idea of the Research Paper by Kenneth G. Paterson & Elizabeth A. Quaglia published in Springer. 

[Time-Specific Encryption](https://link.springer.com/chapter/10.1007/978-3-642-15317-4_1#:~:text=In%20(Plain)%20TSE%2C%20a,a%20time%20in%20that%20interval.)

### Plain Time-Specific Encryption

In (Plain) TSE, a Time Server broadcasts a key at the beginning of each time unit, a Time Instant Key (TIK). The sender of a message can specify any time interval during the encryption process; the receiver can decrypt to recover the message only if it has a TIK that corresponds to a time in that interval. We extend Plain TSE to the public-key and identity-based settings, where receivers are additionally equipped with private keys and either public keys or identities, and where decryption now requires the use of the private key as well as an appropriate TIK. 

### The system is divided into two sections: 
* Time-Server
* Encryption API

### Time Server
It is a separate server hosted by 
