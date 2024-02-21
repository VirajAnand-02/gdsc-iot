import { initializeApp, getAuth } from "firebase/app";
require('dotenv').config();
const YOUR_API_KEY = process.env.API_KEY;
const YOUR_AUTH_DOMAIN = process.env.API_URL;
const YOUR_DATABASE_URL
const YOUR_PROJECT_ID
const YOUR_STORAGE_BUCKET
const YOUR_MESSAGING_SENDER_ID
const YOUR_APP_ID


const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    databaseURL: "YOUR_DATABASE_URL",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
  
firebase.initializeApp(firebaseConfig);
const db = firebase.database();

// Replace 'messages' with the name of your data node
const messagesRef = db.ref('messages');
messagesRef.on('value', (snapshot) => {
  const messages = snapshot.val();
  const table = document.getElementById('messagesTable');
  table.innerHTML = '';

  for (const key in messages) {
    const message = messages[key];
    const row = table.insertRow();

    const nameCell = row.insertCell();
    nameCell.textContent = message.name;

    const textCell = row.insertCell();
    textCell.textContent = message.text;

    const timestampCell = row.insertCell();
    timestampCell.textContent = new Date(message.timestamp).toLocaleString();
  }
});