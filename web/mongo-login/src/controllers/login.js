import { Users } from "../model/User.js";

export async function loginHandler(req,res){
   
        let { username, password } = req.body;
        console.log(req.body);
        if (username && password) {
            return Users.find({ 
                username,
                password
            })
                .then((user) => {
                    if (user.length == 1) {
                        return res.json({logged: 1, message: `Login Successful, welcome back ${user[0].username}.` });
                    } else {
                        return res.json({logged: 0, message: 'Login Failed'});
                    }
                })
                .catch(() => res.json({ message: 'Something went wrong'}));
        }
        return res.json({ message: 'Invalid username or password'});
}