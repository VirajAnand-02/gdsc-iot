import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { get, getDatabase, set, ref } from "firebase/database";

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

function writeUserData(userID, name, email, imageUrl){
    const db = getDatabase();
    const refrence = ref(db, 'user/' + userID);
    set(refrence, {
        username: name, 
        email: email, 
        profile_picture: imageUrl
    })
}

writeUserData("sahjhgghjkh", "kdhbfkds", "email@emial.com", "url_for _image");
writeUserData("sahjhsdfdsfgghjkh", "kdhbsdffkds", "emdsfsdfail@emial.com", "url_dsfdfor _image");


const analytics = getAnalytics(app);