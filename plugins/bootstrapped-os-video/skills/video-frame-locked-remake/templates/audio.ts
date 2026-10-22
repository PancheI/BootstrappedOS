/** The audio agent sets MIX to the final mixed track in public/remake/ (e.g. "remake/mix.wav"); null = silent. */
export const MIX: string | null = null;
export const getRemoteFile = () => MIX;
