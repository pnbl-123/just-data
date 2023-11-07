import { currentUser } from '@clerk/nextjs'
import { redirect } from 'next/navigation'
import { prisma } from 'util/db'

const createNewUser = async (): Promise<void> => {
  const user = await currentUser()
  console.log('user===', user)
  const matchUserInDB = await prisma.user.findUnique({
    where: {
      clerkId: user.id as string,
    },
  })

  if (!matchUserInDB) {
    await prisma.user.create({
      data: {
        clerkId: user.id,
        email: user?.emailAddresses[0]?.emailAddress,
      },
    })
  }
  redirect('/tools')
}

async function NewUser() {
  await createNewUser()

  return <div>...Loading NewUser</div>
}

export default NewUser
