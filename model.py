# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""A PyQt math expression evaluator using Python eval() and the math module."""

import math


ALLOWED_NAMES = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}


class MainModel:

    def eval_expression(self, expression):
        """Evaluate a math expression."""
        # Compile the expression eventually raising a SyntaxError
        # when the user enters an invalid expression
        code = compile(expression, "<string>", "eval")

        # Validate allowed names
        for name in code.co_names:
            if name not in ALLOWED_NAMES:
                raise NameError(f"The use of '{name}' is not allowed")

        # Evaluate the expression eventually raising a ValueError
        # when the user uses a math function with a wrong input value
        # e.g. math.sqrt(-10)
        return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)
