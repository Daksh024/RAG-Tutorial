# Runnable - buliding block for the tasks
# Multiple Runnable in pipeline
# Asynchronous Executions
# Parallel Execution

# -------------------------------------------

from langchain_core.runnables import Runnable

class BasicRunnable(Runnable):
    """DEMO RUNNABLE"""
    def invoke(self, input):
        return input.upper()
    
# Runnable
runnable = BasicRunnable()

#result = runnable.invoke("this is demo!!!")
#print(result)

# -------------------------------------------

# Two Runnable at a time
from langchain_core.runnables import RunnableMap

runnable_map = RunnableMap({
    "runnable1": lambda x: x.upper(),
    "runnable2": lambda x: x[::-1]
})

# result = runnable_map.invoke("Hello")
# print(result)

# -------------------------------------------
# Sequence

from langchain_core.runnables import RunnableSequence

runnable_sequence = RunnableSequence(*[
    lambda x: x[::2],   # step 1
    lambda x: x.upper()  # step 2
])

# result = runnable_sequence.invoke("Hello World!!")
# print(result)

# -------------------------------------------
# Runnable Lambda

from langchain_core.runnables import RunnableLambda

stepping_runnable = RunnableLambda(lambda x: x[::2])
result = stepping_runnable.invoke("Hello World!!!")
print(result)