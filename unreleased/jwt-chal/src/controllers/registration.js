import { query } from "../database/database.js";
import jwt from 'jsonwebtoken'
import dotenv from 'dotenv'
import {nanoid} from 'nanoid'
dotenv.config();
export const registerPage = async(req,res)=>{
    res.render("registration")
}

export const handleRegistration=async(req,res)=>{
    console.log(req.body);
    let {username,password} = req.body;
    if(username!==undefined && password !== undefined)
    {
        //check if user already exists
        const sqlQuery = `SELECT * FROM Users WHERE username=?`
        const valArray = [username];

        const result = await query({query:sqlQuery,values:valArray})
        console.log(result);
        if(result.length !==0){
            res.status(409).json({
                message:"User already exists"
            })
        }
        else{

            const createQuery = `INSERT INTO Users(username, password, authcode) VALUES (?, MD5(?), ?)`;
            const authcode = nanoid(12);
            console.log(authcode)
            const valarray = [username,password,authcode];
            const result = await query({values:valarray,query:createQuery})
            console.log(result.insertId)
            //set cookie token
            let userDetails = 
            {
                username:username,
                id:result.insertId,
                admin:false
            }
            let token = jwt.sign(userDetails, process.env.JWT_SECRET_KEY, { algorithm: 'HS256' });

            res.cookie('user_cookie',token, { maxAge: 900000 });
            const profileUrl = `/profile/${result.insertId}`;
            res.status(200).json({
                message: "Registration successful",
                profileUrl: profileUrl
            });
        }
    }
}