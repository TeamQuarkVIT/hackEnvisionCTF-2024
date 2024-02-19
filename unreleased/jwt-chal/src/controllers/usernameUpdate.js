import jwt from "jsonwebtoken";
import { query } from "../database/database.js";

export function getUserNameUpdationPage(req, res) {
  res.render("updateUsername.ejs");
}

export async function handleUserNameUpdation(req, res) {
    let cookie = req.cookies.user_cookie;
    console.log(req.body);
  
    if (cookie) {
      let cookieData = jwt.decode(cookie);
  
      if (cookieData.admin) {
        res.json(`flag:${process.env.FLAG}`);
      } else {
        const sqlQuery = `SELECT * FROM Users WHERE id=?`;
        let valArray = [cookieData.id];
  
        try {
          let result = await query({ values: valArray, query: sqlQuery });
  
          if (result.length === 0) {
            res.json("some error occurred");
          } else {
            if (result[0].authcode === req.body.authcode) {
              console.log("authcode matched");
              const updateQuery = `UPDATE Users SET username=? WHERE id=?`;
              const arr = [req.body.newusername, cookieData.id];
  
              try {
                await query({ query: updateQuery, values: arr });
  
                // Use setTimeout only if absolutely necessary
                setTimeout(() => {
                  res.json(`name updated to ${req.body.newusername}`);
                }, 1000);
              } catch (updateError) {
                console.error("Error updating username:", updateError);
                res.json("Error updating username");
              }
            } else {
              res.json("wrong authcode!!!");
            }
          }
        } catch (error) {
          console.error("Error querying database:", error);
          res.json("Error querying database");
        }
      }
    } else {
      res.send("user not logged in ");
    }
  }
