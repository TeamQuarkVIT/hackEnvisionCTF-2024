import { query } from "../database/database.js"
import jwt from 'jsonwebtoken'
export const profilePage= async(req,res)=>{
    const sqlQuery = `SELECT * FROM Users where id=?`
    const valArray = [req.params.id]
    console.log(req.params.id)
    const result =await query({query:sqlQuery,values:valArray})
    console.log(result)
    if(result.length===0)
    {
        res.send("user doesn't exist")
    }
    console.log(result[0].username)

    console.log("cookie:",req.cookies)
    if(req.cookies?.user_cookie)
    {
        let decryptedCookie = jwt.decode(req.cookies.user_cookie)
       if(decryptedCookie.id ==result[0].id)
       {
           res.render('profile',{name:result[0].username})
       }
       else{
        res.send('cannot access this')
       }
    }
    else{

        res.send("Cannot access this");
    }
}