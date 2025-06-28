import { useState } from "react";

function MyButton() {
  const [likes, setLikes] = useState(0);

  function handleClick() {
    setLikes(likes + 1);
  }

  return <button onClick={handleClick}>Clicked {likes} times!</button>;
}

function App() {
  return <MyButton />;
}

export default App;
