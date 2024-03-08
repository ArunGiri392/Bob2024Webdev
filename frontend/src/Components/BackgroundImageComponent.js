// BackgroundImageComponent.js
import React from 'react';
import homepage from '../images/background.jpg'; 

const BackgroundImageComponent = () => {
  const styles = {
    backgroundImage: `url(${homepage})`,
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    width: '100%',
    height: '100vh', 
  };

  return <div style={styles} />;
};

export default BackgroundImageComponent;
