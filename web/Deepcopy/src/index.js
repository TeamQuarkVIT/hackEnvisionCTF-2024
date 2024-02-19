import express from "express";
import dotenv from "dotenv";
const app = express();
dotenv.config();

app.use(express.json());

let flag = process.env.FLAG;
// 
app.get("/", (req, res) => {
  res.json("Hello ");
});

app.post("/", (req, res) => {
  const obj = {
    name: "Quark",
    details: {
      flag: flag,
    },
  };
  if(req.body.newObj.indexOf("re")!==-1)
  {
    res.send("No cheating, no cheating")
  }
  let newObj;
  try {
    newObj = eval(req.body.newObj);
  } catch (error) {
    res.send("OOPS, Error occured :(");
  }

  obj.details.flag = "Sorry, smarty pants!";

  try {
    if (newObj.details.flag === flag) {
      res.json(flag);
    } else {
      res.send("Sike, that's the wrong number");
    }
  } catch (error) {
    res.send("OOPS, error occured :(");
  }
});

app.listen(process.env.PORT, () => {
  console.log("server running on port",process.env.PORT);
});
