# Challenge Name: time_trial
### Category: Rust
### Author: [Piyush Waghulde](https://github.com/piyushw0203)

### Description

> "Time is what we want most, but what we use worst." - William Penn


# Writeup

- This CTF challenge is centered around time-based encryption. A string is obfuscated using a key derived from the execution time (seconds since Unix Epoch), a calculation is performed involving that key, and the answer is the length of the final calculated result.

- Additionally, a restriction of 10s is put on the input for the user, so they cannot use the brute force approach.

  ### Intended Solution
  This function:

  ``` rust
  fn fn4(input: &str, key: u8) -> String {
    input
        .chars()
        .enumerate()
        .map(|(i, c)| (c as u8 ^ (key + i as u8)) as char)
        .collect()
  }
  ```
   provides a clue. While labeled as encryption, it employs a basic XOR operation, which has the unique 
   property of reversing itself when applied twice with the same key. In the code, an encoded string 
   undergoes fn4 and is immediately passed back into fn4, effectively undoing the previous step.

   ```rust
   let ee_string = fn4(&e_string, key);
   let dd_string = fn4(&ee_string, key); 
   ```
   Therefore, the result gets reverted even if the key is dynamically generated based on the System's time 
   from the UNIX Epoch. Lastly, the flag is revealed after
   "simple base64 encoding - some misc. operations - 
   base64 decoding" -
   is done by the player and the player enters the length of the result. 

### Flag
`quarkCTF{time_is_an_illusion}`
