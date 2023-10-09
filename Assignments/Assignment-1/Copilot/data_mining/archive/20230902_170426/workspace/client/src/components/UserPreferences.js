import React from 'react';

function UserPreferences() {
  return (
    <div>
      <select>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
      </select>
      <input type="checkbox" id="vegetarian" name="vegetarian" />
      <label for="vegetarian">Vegetarian</label>
      {/* Other dietary preferences go here */}
    </div>
  );
}

export default UserPreferences;
