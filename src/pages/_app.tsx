import { type AppType } from "next/app";

import { api } from "base/utils/api";

import "base/styles/globals.css";

const MyApp: AppType = ({ Component, pageProps }) => {
  return <Component {...pageProps} />;
};

export default api.withTRPC(MyApp);
