/**
 * Cleans raw disease class names from the backend
 * into user-friendly display names.
 *
 * Examples:
 *   "Tomato___Tomato_mosaic_virus"  → "Tomato Mosaic Virus"
 *   "Tomato___healthy"              → "Healthy Tomato"
 *   "Potato___Late_blight"          → "Potato Late Blight"
 *   "Corn_(maize)___Common_rust_"   → "Corn (Maize) Common Rust"
 */
export function formatDiseaseName(raw) {
  if (!raw) return "";

  // 1. Replace underscores with spaces, collapse multiple spaces
  let name = raw.replace(/_+/g, " ").trim();

  // 2. Remove duplicate consecutive words (case-insensitive)
  //    e.g. "Tomato Tomato mosaic virus" → "Tomato mosaic virus"
  name = name.replace(/\b(\w+)(\s+\1)+\b/gi, "$1");

  // 3. Trim any trailing/leading whitespace that may have appeared
  name = name.trim();

  // 4. Title-case every word
  name = name
    .split(/\s+/)
    .map((word) => {
      // Keep parenthesised words like "(maize)" properly cased
      if (word.startsWith("(")) {
        return "(" + word.slice(1, 2).toUpperCase() + word.slice(2);
      }
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    })
    .join(" ");

  // 5. If the name ends with "Healthy", move it to the front
  //    e.g. "Tomato Healthy" → "Healthy Tomato"
  if (name.endsWith("Healthy")) {
    const plant = name.replace(/\s*Healthy$/, "").trim();
    name = plant ? `Healthy ${plant}` : "Healthy";
  }

  return name;
}
