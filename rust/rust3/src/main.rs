use async_std::io;
use std::time::Duration;
use std::fs;

// Function allows User-Input for 10 seconds only
async fn input_for_10sec() -> Result<String, std::io::Error> {
    let input = io::timeout(Duration::from_secs(10), async {
        let mut buffer = String::new();
        let stdin = io::stdin();
        stdin.read_line(&mut buffer).await?;
        Ok(buffer)
    }).await;

    input
}
// --

#[async_std::main]
async fn main() {

    println!("\nEnter the password to get the 🚩: ");
    
    let input = input_for_10sec().await;
    let input = match input {
        Ok(input_buff) => input_buff,
        Err(_) => {println!("\nPlease give your input within 10 seconds ⏳⌛\n"); return},
    }; 
    
    let password = input.trim();

    if password.as_bytes().len() >= 12 {
        println!("Nice Try 👻");
        return;
    }
    
    println!("\nWhat's this??? 🤔 \"{}\"\n", password.as_bytes().len());
    
    fn do_something(password: &str) -> String {
        let mut some_string = String::new();
        
        for byte in password.trim().bytes() {
            byte
            .to_string()
            .chars()
            .for_each(|ch| {
                some_string.push(char::from_u32(ch.to_digit(10).expect("Valid Digit") + 90 ).expect("Valid ASCII code"))
            });
        }
        
        some_string
    }
    
    let flag = fs::read_to_string("flag.txt").expect("Should be a valid file");

    let some_string = do_something(password);
    let expected_string = r"\^Z[_c[``[\b".to_string();
    
    if some_string == expected_string {
        println!("{flag}\n");
    }
    else {
        println!("Think a bit more creatively☕");
    }
}
