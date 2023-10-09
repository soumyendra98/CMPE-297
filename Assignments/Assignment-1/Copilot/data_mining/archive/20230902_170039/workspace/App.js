import React from 'react';
import SearchBar from './SearchBar';
import Filter from './Filter';
import RecipeList from './RecipeList';
import axios from 'axios';

class App extends React.Component {
  state = { recipes: [] };

  onSearchSubmit = async (user, ingredients) => {
    const response = await axios.post('http://localhost:5000/get_recipes', { user, ingredients });
    this.setState({ recipes: response.data });
  };

  render() {
    return (
      <div>
        <SearchBar onSubmit={this.onSearchSubmit} />
        <Filter />
        <RecipeList recipes={this.state.recipes} />
      </div>
    );
  }
}

export default App;
