import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { get, getDatabase } from "firebase/database";

const firebaseConfig = {
  apiKey: "AIzaSyCo-DxeMNTue0TWkFRv852juThQfIUTqzg",
  authDomain: "gdsc-iot-2f969.firebaseapp.com",
  databaseURL: "https://gdsc-iot-2f969-default-rtdb.firebaseio.com",
  projectId: "gdsc-iot-2f969",
  storageBucket: "gdsc-iot-2f969.appspot.com",
  messagingSenderId: "876280275369",
  appId: "1:876280275369:web:86934d36d891dc4bb164b8",
  measurementId: "G-YM7E03T6CN"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const db = getDatabase();
const refrence


const analytics = getAnalytics(app);