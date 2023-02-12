import { useState } from 'react'
import { useMutation, useQuery, useQueryClient } from 'react-query'
import { getTests, postTest } from '../core/api'
import { Test } from '../core/types'

export const Page = () => {
  const query = useQuery('test', getTests)
  const [formVal, setFormVal] = useState<string>("")

  const queryClient = useQueryClient()

  const onSubmit = (event: any) => {
    event.preventDefault();

    const test: Test = {'field_1': formVal}
    if (formVal.length > 0) {
        createTestMutation.mutate(test)
        setFormVal("")
    }
  }

  const createTestMutation = useMutation(postTest, {
    onSuccess: () => {
      queryClient.invalidateQueries('test')
    },
  })

  return (<>
    <p>Tests:</p>
    <ul>
    {query.data?.map((test: Test) => <li key={test["field_1"]}>{test["field_1"]}</li>)}
    </ul>

    <form>
      <label htmlFor="field1">Test field 1:</label><br/>
      <input
        type="text"
        onChange={
          (e: any) => setFormVal(e.target.value)
        }
        value={formVal}
        id="field1"
        name="field1"
      />
      <br/><br/>
      <button type="button" onClick={onSubmit}>Add a new test</button>
    </form> 
  </>)
}