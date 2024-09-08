import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { name, email, message } = req.body;

    // Configure Nodemailer
    const transporter = nodemailer.createTransport({
      service: 'gmail', // or another email provider
      auth: {
        user: 'frederickyxyzsubmissions@gmail.com', // Your email from environment variables
        pass: 'Jarl@200820', // Your email password from environment variables
      },
    });

    const mailOptions = {
      from: email,
      to: 'frederickyxyz@gmail.com', // Your private work email
      subject: `Form submission from ${name}`,
      text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`,
    };

    try {
      await transporter.sendMail(mailOptions);
      res.status(200).json({ message: 'Email sent successfully!' });
    } catch (error) {
      res.status(500).json({ message: 'Error sending email.' });
    }
  } else {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
