const nodemailer = require("nodemailer");
  
export default async (req, res) => {

const { firstName, lastName, email, message } = JSON.parse(req.body);

const transporter = nodemailer.createTransport({
    port: 465,
    host: "smtp.gmail.com",
    auth: {
        user: "frederickyxyzsubmissions@gmail.com",
        pass: "Jarl@200820",
    },
    secure: true,
});

await new Promise((resolve, reject) => {
    // verify connection configuration
    transporter.verify(function (error, success) {
        if (error) {
            console.log(error);
            reject(error);
        } else {
            console.log("Server is ready to take our messages");
            resolve(success);
        }
    });
});

const mailData = {
    replyTo: email,
    to: "frederickyxyz@gmail.com",
    subject: `form message`,
    text: message,
    html: `${message}`,
};

await new Promise((resolve, reject) => {
    // send mail
    transporter.sendMail(mailData, (err, info) => {
        if (err) {
            console.error(err);
            reject(err);
        } else {
            console.log(info);
            resolve(info);
        }
    });
});

res.status(200).json({ status: "OK" });
};
