import Head from 'next/head'
import { Page } from '../components/Page'

export default function Home() {
  return (
    <>
      <Head>
        <title>Template Application</title>
        <meta name="description" content="Template Application" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <main style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <>
          <Page></Page>
        </>
      </main>
    </>
  )
}
