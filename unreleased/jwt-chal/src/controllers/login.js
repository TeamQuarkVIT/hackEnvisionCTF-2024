import { query } from "../database/database.js";
import jwt from'jsonwebtoken'
import md5 from 'md5'
export const loginPage = (req, res) => {
  res.render("login");
};

export const handleLogin = async (req, res) => {
  console.log(req.body);
  let { username, password } = req.body;
  if (username !== undefined && password !== undefined) {
    const sqlQuery = `SELECT * FROM Users WHERE username=?`;
    const valArray = [username];
    const result = await query({ query: sqlQuery, values: valArray });
    console.log("result:", result);
    if (result.length <= 0) {
      res.json({
        message:
          "No such user exists!!,please register first before logging in",
      });
    } else {
      let user = result[0];
      if (user.password === md5(password)) {
        let userDetails = {
          username: username,
          id:user.id,
          admin: false,
        };
        let token = jwt.sign(userDetails, process.env.JWT_SECRET_KEY, {
          algorithm: "HS256",
        });

        res.cookie("user_cookie", token, { maxAge: 900000 });
        console.log("login succesfull");
        const profileUrl = `/profile/${result[0].id}`;
        res.status(200).json({
          message: "login successful",
          profileUrl: profileUrl,
        });
      } else {
        res.json({
          message: "invalid password or username",
        });
      }
    }
  } else {
    res.json({
      message: "invalid or insufficient credentials",
    });
  }
};
