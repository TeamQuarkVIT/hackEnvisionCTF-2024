# Challenge Name: Maalik
### Category: Rust
### Author: Piyush Waghulde

### Description

> Maalik you are the real owner of the flag


# Writeup

- This challenge tests your ability to decode a series of string manipulations and calculations while navigating the nuances of Rust's memory management model involving Ownership and Borrowing concepts.

- Additionally, a restriction of 10s is put on the input for the user, so they cannot use the brute force approach.

### Approach
Here's where Rust's memory management adds a layer to the puzzle:

  - Implicit Mutability:
  Functions like fn1  take &mut String as arguments.  They modify the input string in place.

  ``` rust
  fn fn1(s: &mut String) {
      let reversed: String = s.chars().rev().enumerate().map(|(i, c)| if i % 2 == 0 { 
  c.to_uppercase().next().unwrap() } else { c }).collect();
      s.clear();
      s.push_str(&reversed);
  }
  ```

  - Mixing Ownership and References:
  

   ```rust
  fn fn2(s: String) -> String {
      let mut encoded: Vec<char> = s.chars().map(|c| {
          match c {
              'a'..='z' => ((c as u8 - b'a' + 13) % 26 + b'a') as char,
              'A'..='Z' => ((c as u8 - b'A' + 13) % 26 + b'A') as char,
              '0'..='9' => ((c as u8 - b'0' + 5) % 10 + b'0') as char,
              _ => c,
          }
      }).collect();
      encoded.reverse();
      encoded.into_iter().collect()
  }
   ```
fn2 takes ownership of a String parameter. Then, within PuzzleResult::new: A clone of the string is created before being passed to fn2

- Hidden Borrowing:
    ```rust
    let parsed_i_variable: i32 = m_result.chars().filter(|c| c.is_digit(10)).collect::<String> ().parse().expect("Failed to parse integer"); 
    ```
    Methods like .chars(), .filter(), .collect(), and .parse() implicitly borrow values.

## Solution
Closely follow how the result string within PuzzleResult is modified, cloned, and borrowed throughout the calculation process.

Here's the step-by-step approach to deduce the correct answer:

- Initial String: "Rust"
- After fn1: "TsUr"
- After fn2: "Ghol"
- Appending "42": "Ghol42"
- Multiplying by 3: "126" (since 'Ghol42' parses as 42)
- Appending "10": "12610"
- Final Calculation: "12600" (12610 - 10)

### Flag
`quarkCTF{j0_bh1_l@n@_d0_l@n@}`
