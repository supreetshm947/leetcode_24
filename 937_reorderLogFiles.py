class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        log_digits = []
        log_alpha = []

        for log in logs:
            identifier, content = log.split(" ", 1)

            if content[0].isdigit():
                log_digits.append(log)
            else:
                log_alpha.append((identifier, content))

        log_alpha.sort(key=lambda x: (x[1], x[0]))
        log_alpha = [f"{identifier} {content}" for identifier, content in log_alpha]

        return log_alpha + log_digits


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
out = Solution().reorderLogFiles(logs)
print(out)