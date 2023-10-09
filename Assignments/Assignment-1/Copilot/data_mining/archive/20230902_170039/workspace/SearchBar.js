import React from 'react';

class SearchBar extends React.Component {
  state = { ingredients: '' };

  onFormSubmit = event => {
    event.preventDefault();
    this.props.onSubmit(this.state.ingredients);
  };

  render() {
    return (
      <form onSubmit={this.onFormSubmit}>
        <input
          type="text"
          value={this.state.ingredients}
          onChange={e => this.setState({ ingredients: e.target.value })}
        />
        <button type="submit">Search</button>
      </form>
    );
  }
}

export default SearchBar;
