import { useState } from 'react';
import { identifyCar, getCarSpecs } from '../services/api';

export const useCarIdentification = () => {
  const [predClass, setPredClass] = useState(null);
  const [specs, setSpecs] = useState(null);
  const [loading, setLoading] = useState(false);
  const [specLoading, setSpecLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleIdentify = async (imageFile) => {
    if (!imageFile) return;
    
    setLoading(true);
    setError(null);
    setPredClass(null);
    setSpecs(null);
    
    try {
      const result = await identifyCar(imageFile);
      setPredClass(result.pred_class);
    } catch (err) {
      const details = err.response ? JSON.stringify(err.response.data) : err.message;
      setError('Error identifying car: ' + details);
    } finally {
      setLoading(false);
    }
  };

  const handleShowSpecs = async () => {
    if (!predClass) return;
    
    setSpecLoading(true);
    setError(null);
    
    try {
      const result = await getCarSpecs(predClass);
      if (result && !result.error) {
        setSpecs(result);
      } else {
        setError('No specs found or backend error.');
      }
    } catch (err) {
      setError('Error fetching car specs.');
    } finally {
      setSpecLoading(false);
    }
  };

  const reset = () => {
    setPredClass(null);
    setSpecs(null);
    setError(null);
  };

  return {
    predClass,
    specs,
    loading,
    specLoading,
    error,
    handleIdentify,
    handleShowSpecs,
    reset
  };
};
