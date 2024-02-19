import jwt from 'jsonwebtoken'
import {query} from '../database/database.js'
export async function handleGetAuthCode(req,res){
    let cookie = req.cookies.user_cookie

    if(cookie)
    {
        let cookieData = jwt.decode(cookie);
        if(cookieData.admin)
        {
            res.json(`flag:${process.env.FLAG}`)
        }
        else{
            const sqlQuery = `SELECT * FROM Users where id=?`
            let valArray = [cookieData.id];
            let result = await query({values:valArray,query:sqlQuery});
                if(result.length===0){
                    res.json("some error occured")
                }
                else{
                    res.json(`authcode:${result[0].authcode}`);
                }
        }
    }
    else{
        res.send("user not logged in ")
    }
}