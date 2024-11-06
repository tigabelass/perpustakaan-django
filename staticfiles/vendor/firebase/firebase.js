// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCrIjKiMJKXARrNlMVKhMCxbp5C_HaIx3U",
  authDomain: "librarymawut.firebaseapp.com",
  projectId: "librarymawut",
  storageBucket: "librarymawut.firebasestorage.app",
  messagingSenderId: "342420212218",
  appId: "1:342420212218:web:f51a735f55dce6cb49bc43",
  measurementId: "G-8CL6L75VBB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

