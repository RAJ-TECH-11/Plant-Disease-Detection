import React from "react";

const UploadBox = ({ onUpload, isLoading }) => {

  const handleFileChange = (e) => {

    const file = e.target.files[0];

    if (!file) return;

    if (file.size > 5 * 1024 * 1024) {

      alert("Maximum file size is 5 MB");

      return;
    }

    onUpload(file);

  };

  return (

    <div className="flex items-center justify-center w-full">

      <label
        htmlFor="dropzone-file"
        className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer bg-slate-800 border-slate-600 hover:border-emerald-400 transition"
      >

        <div className="text-center">

          <p className="text-emerald-400 font-semibold">

            Click to Upload

          </p>

          <p className="text-slate-400 mt-2">

            PNG / JPG / JPEG

          </p>

        </div>

        <input
          id="dropzone-file"
          type="file"
          className="hidden"
          accept="image/*"
          onChange={handleFileChange}
          disabled={isLoading}
        />

      </label>

    </div>

  );

};

export default UploadBox;