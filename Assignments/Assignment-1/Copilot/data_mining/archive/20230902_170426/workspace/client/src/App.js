import React from 'react';
import RecipeList from './components/RecipeList';
import SearchBar from './components/SearchBar';
import UserPreferences from './components/UserPreferences';

function App() {
  return (
    <div className="App">
      <SearchBar />
      <UserPreferences />
      <RecipeList />
    </div>
  );
}

export default App;
