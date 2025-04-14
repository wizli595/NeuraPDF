from app.chat.tracing import langfuse1
from langfuse.model import CreateTrace
class TraceableChain:
    def __call__(self, *args, **kwds):
        trace =  langfuse1.trace(
            CreateTrace(
                id=self.metadata["conversation_id"],
                metadata=self.metadata,
            )
        )
        callbacks = kwds.get("callbacks", [])
        callbacks.append(trace.getNewHandler())
        kwds["callbacks"] = callbacks

        return super().__call__(*args, **kwds)