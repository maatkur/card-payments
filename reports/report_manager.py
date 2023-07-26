from reports.unconciliateds_report import UnconciliatedsReport
from reports.conciliateds_report import ConciliatedsReport


class ReportManager:
    _unconciliateds_report = None
    _conciliateds_report = None

    @staticmethod
    def unconciliateds():
        if ReportManager._unconciliateds_report is None:
            ReportManager._unconciliateds_report = UnconciliatedsReport()
        return ReportManager._unconciliateds_report

    @staticmethod
    def conciliateds():
        if ReportManager._conciliateds_report is None:
            ReportManager._conciliateds_report = ConciliatedsReport()
        return ReportManager._conciliateds_report
