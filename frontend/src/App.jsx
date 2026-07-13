import { useState } from "react";

import UploadBox from "./components/UploadBox";
import ResultCard from "./components/ResultCard";

import { uploadImage } from "./services/api";

function App() {

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [imagePreview, setImagePreview] = useState(null);

  const [error, setError] = useState("");

  const handleUpload = async (file) => {

    setLoading(true);

    setError("");

    setResult(null);

    const preview = URL.createObjectURL(file);

    setImagePreview(preview);

    try {

      const response = await uploadImage(file);

      setResult(response);

    } catch {

      setError("Prediction Failed");

    } finally {

      setLoading(false);

    }

  };

  const handleReset = () => {
    setResult(null);
    setImagePreview(null);
    setError("");
  };

  return (

    <div className="min-h-screen bg-slate-900 text-white flex flex-col items-center p-10">

      <h1 className="text-5xl font-bold text-emerald-400 mb-2">

        Plant Disease Detection

      </h1>

      <p className="text-slate-400 mb-10">

        Upload a leaf image and detect disease using Deep Learning.

      </p>

      {!result && (
        <div className="w-full max-w-xl">

          <UploadBox

            onUpload={handleUpload}

            isLoading={loading}

          />

        </div>
      )}

      {loading && (

        <div className="mt-10">

          <p className="text-emerald-400">

            Predicting...

          </p>

        </div>

      )}

      {error && (

        <p className="text-red-400 mt-6">

          {error}

        </p>

      )}

      <ResultCard

        result={result}

        imagePreview={imagePreview}

      />

      {result && (
        <button
          onClick={handleReset}
          className="mt-8 px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold rounded-lg transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/25 active:scale-95 cursor-pointer"
        >
          Choose Another Image
        </button>
      )}

    </div>

  );

}

export default App;