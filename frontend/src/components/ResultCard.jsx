import React from "react";
import { formatDiseaseName } from "../utils/formatDiseaseName";

const ResultCard = ({ result, imagePreview }) => {
  if (!result) return null;

  const { prediction, top_predictions, description, symptoms, prevention } =
    result;

  return (
    <div className="w-full max-w-xl bg-slate-800 rounded-xl shadow-xl overflow-hidden mt-8">

      {imagePreview && (
        <img
          src={imagePreview}
          alt="Uploaded Leaf"
          className="w-full h-64 object-cover"
        />
      )}

      <div className="p-6">

        <h2 className="text-2xl font-bold text-emerald-400">
          {formatDiseaseName(prediction.disease)}
        </h2>

        <p className="mt-3 text-lg">
          <span className="font-semibold">Confidence:</span>{" "}
          {prediction.confidence}%
        </p>

        {/* Animated confidence progress bar */}
        <div className="mt-3 w-full bg-slate-700/60 rounded-full h-3 overflow-hidden">
          <div
            className={`h-full rounded-full transition-all duration-1000 ease-out ${
              prediction.confidence >= 80
                ? "bg-emerald-400 shadow-[0_0_12px_rgba(52,211,153,0.5)]"
                : prediction.confidence >= 50
                  ? "bg-amber-400 shadow-[0_0_12px_rgba(251,191,36,0.4)]"
                  : "bg-red-400 shadow-[0_0_12px_rgba(248,113,113,0.4)]"
            }`}
            style={{ width: `${prediction.confidence}%` }}
          />
        </div>

        <hr className="my-5 border-slate-700" />

        <h3 className="text-xl font-semibold mb-2">
          Description
        </h3>

        <p className="text-slate-300">
          {description}
        </p>

        <h3 className="text-xl font-semibold mt-6 mb-2">
          Symptoms
        </h3>

        <ul className="list-disc ml-6 text-slate-300">
          {symptoms.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>

        <h3 className="text-xl font-semibold mt-6 mb-2">
          Prevention
        </h3>

        <ul className="list-disc ml-6 text-slate-300">
          {prevention.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>

        <h3 className="text-xl font-semibold mt-6 mb-3">
          Top Predictions
        </h3>

        <div className="space-y-2">

          {top_predictions.map((item, index) => {
            const medals = ["🥇", "🥈", "🥉"];
            const medal = medals[index] || "";

            const isFirst = index === 0;

            return (
              <div
                key={index}
                className={`flex items-center justify-between rounded-lg px-4 py-3 transition-all duration-300 ${
                  isFirst
                    ? "bg-emerald-900/40 border border-emerald-500/30"
                    : "bg-slate-700/60"
                }`}
              >

                <span className="flex items-center gap-2">
                  <span className="text-lg">{medal}</span>
                  <span className={isFirst ? "font-semibold text-emerald-300" : "text-slate-200"}>
                    {formatDiseaseName(item.disease)}
                  </span>
                </span>

                <span className={`font-bold text-sm px-3 py-1 rounded-full ${
                  isFirst
                    ? "bg-emerald-500/20 text-emerald-300"
                    : "bg-slate-600/60 text-slate-300"
                }`}>
                  {item.confidence}%
                </span>

              </div>
            );
          })}

        </div>

      </div>

    </div>
  );
};

export default ResultCard;